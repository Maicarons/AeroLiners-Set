cmake_minimum_required(VERSION 3.24)

# Release metadata lives in bundle.json — the single source of truth shared by
# CMake and .github/workflows/release.yml through scripts/bundle.py.
file(READ "${CMAKE_CURRENT_SOURCE_DIR}/bundle.json" BUNDLE_JSON)
string(JSON BUNDLE_NAME        GET    "${BUNDLE_JSON}" name)
string(JSON BUNDLE_VERSION     GET    "${BUNDLE_JSON}" version)
string(JSON BUNDLE_HOMEPAGE    GET    "${BUNDLE_JSON}" homepage)
string(JSON BUNDLE_GRFID       GET    "${BUNDLE_JSON}" grfid)
string(JSON PROJECT_SHORT_NAME GET    "${BUNDLE_JSON}" grfid_text)
string(JSON GRF_FILE_NAME      GET    "${BUNDLE_JSON}" grf_file)
string(JSON NML_FILE_NAME      GET    "${BUNDLE_JSON}" nml_file)
string(JSON SRC_FILE_NAME      GET    "${BUNDLE_JSON}" src_file)
string(JSON BIN_DIR            GET    "${BUNDLE_JSON}" bin_dir)
string(JSON DOCS_SRC_DIR       GET    "${BUNDLE_JSON}" docs_src_dir)
string(JSON DOC_COUNT          LENGTH "${BUNDLE_JSON}" docs)

project(${BUNDLE_NAME} VERSION ${BUNDLE_VERSION} HOMEPAGE_URL ${BUNDLE_HOMEPAGE})

if(DOC_COUNT GREATER 0)
  math(EXPR DOC_LAST "${DOC_COUNT} - 1")
  foreach(i RANGE 0 ${DOC_LAST})
    string(JSON DOC_NAME GET "${BUNDLE_JSON}" docs ${i})
    list(APPEND DOC_FILE_NAMES "${DOC_NAME}")
  endforeach()
endif()

set(PROJECT_SCRIPT_DIR "${PROJECT_SOURCE_DIR}/scripts")
set(OUTPUT_DIR "${PROJECT_SOURCE_DIR}/${BIN_DIR}")
set(DOCS_DIR "${PROJECT_SOURCE_DIR}/${DOCS_SRC_DIR}")
set(BUNDLE_SCRIPT "${PROJECT_SCRIPT_DIR}/bundle.py")
set(GRF_FILE "${OUTPUT_DIR}/${GRF_FILE_NAME}")
set(NML_FILE "${OUTPUT_DIR}/${NML_FILE_NAME}")
set(SRC_FILE "${PROJECT_SOURCE_DIR}/${SRC_FILE_NAME}")
set(CUSTOM_TAGS_FILE "${PROJECT_SOURCE_DIR}/custom_tags.txt")
set(DOC_SRC_FILES "")
foreach(DOC_NAME IN LISTS DOC_FILE_NAMES)
  list(APPEND DOC_SRC_FILES "${DOCS_DIR}/${DOC_NAME}")
endforeach()

# Archives produced by scripts/bundle.py (BaNaNa / OpenTTD content-download layout):
#   <grfid>-<name>-<version>.tar  and  .tar.gz
set(BUNDLE_TAR "${OUTPUT_DIR}/${BUNDLE_GRFID}-${PROJECT_NAME}-${PROJECT_VERSION}.tar")
set(BUNDLE_GZ  "${BUNDLE_TAR}.gz")

file(MAKE_DIRECTORY "${OUTPUT_DIR}")
message(STATUS "Outputting files to ${OUTPUT_DIR}")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${OUTPUT_DIR}")
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${OUTPUT_DIR}")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${OUTPUT_DIR}")

find_program(PYTHON_EXECUTABLE NAMES python python3 REQUIRED)

# Get days since 2000 (same formula as scripts/bundle.py info --key repo_revision)
string(TIMESTAMP UNIX_EPOCH "%s" UTC)
math(EXPR DAYS_SINCE_2K "(${UNIX_EPOCH} - 946684800) / 86400")

if(MSVC)
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS}"
    /DREPO_REVISION=${DAYS_SINCE_2K}
    /DNEWGRF_VERSION=${PROJECT_VERSION}
    /utf-8
    /c /C /P /EP
    /Fi${NML_FILE}
  )
else()
  set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS}"
    -D REPO_REVISION=${DAYS_SINCE_2K}
    -D NEWGRF_VERSION=${PROJECT_VERSION}
    -C -E -nostdinc -x c-header
    -o ${NML_FILE}
  )
endif()

# Process .pnml to .nml using the C preprocessor (a target so it runs every time)
add_custom_target("NML"
  BYPRODUCTS ${NML_FILE}
  COMMAND ${CMAKE_C_COMPILER} ${CMAKE_C_FLAGS} ${SRC_FILE}
  DEPENDS ${SRC_FILE}
  SOURCES ${SRC_FILE}
  COMMENT "Processing ${SRC_FILE_NAME} to ${NML_FILE_NAME}"
  VERBATIM
)

add_custom_command(
  OUTPUT ${CUSTOM_TAGS_FILE}
  COMMAND ${CMAKE_COMMAND}
    -DPROJECT_VERSION=${PROJECT_VERSION}
    -DPROJECT_NAME=${PROJECT_NAME}
    -DGRF_FILE_NAME=${GRF_FILE_NAME}
    -DCUSTOM_TAGS_FILE=${CUSTOM_TAGS_FILE}
    -P ${PROJECT_SCRIPT_DIR}/GenerateCustomTags.cmake
  COMMENT "Generating custom_tags.txt file"
  VERBATIM
)

# Compile .nml to .grf by running nmlc on it
add_custom_command(
  OUTPUT ${GRF_FILE}
  COMMAND ${CMAKE_COMMAND}
    -DPROJECT_SOURCE_DIR=${PROJECT_SOURCE_DIR}
    -DPROJECT_BINARY_DIR=${OUTPUT_DIR}
    -DGRF_FILE=${GRF_FILE}
    -DNML_FILE=${NML_FILE}
    -P ${PROJECT_SCRIPT_DIR}/Compile.cmake
  MAIN_DEPENDENCY ${NML_FILE}
  DEPENDS ${CUSTOM_TAGS_FILE} "NML"
  COMMENT "Compiling ${NML_FILE_NAME} to ${GRF_FILE_NAME} using nmlc"
  VERBATIM
)

add_custom_target("GRF"
  DEPENDS ${GRF_FILE}
  COMMENT "Generating .grf from .pnml source file"
  VERBATIM
)

# Bundles: one shared implementation. scripts/bundle.py reads bundle.json,
# substitutes the readme placeholders, stages <name>-<version>/ and writes the
# tar + tar.gz, then self-verifies layout, GRF ID and MD5.
add_custom_command(
  OUTPUT ${BUNDLE_TAR} ${BUNDLE_GZ}
  COMMAND ${PYTHON_EXECUTABLE} ${BUNDLE_SCRIPT} build
  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
  DEPENDS ${GRF_FILE} ${DOC_SRC_FILES} ${BUNDLE_SCRIPT} "${CMAKE_CURRENT_SOURCE_DIR}/bundle.json"
  COMMENT "Building BaNaNaS bundles via scripts/bundle.py"
  VERBATIM
)

add_custom_target("Bundles" ALL
  DEPENDS ${BUNDLE_TAR} ${BUNDLE_GZ}
  COMMENT "Bundling files"
  VERBATIM
)
