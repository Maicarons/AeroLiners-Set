# Download

The core product of AeroLiners Set is the **NewGRF package file** `AeroLinersSet.grf`, which contains every aircraft model and authentic livery included in the project and can be dropped straight into OpenTTD. Several ways to obtain it are listed below — pick whichever suits you.

<p align="center">
  <a class="download-btn" href="https://github.com/Maicarons/AeroLiners-Set/releases/latest" target="_blank" rel="noopener">
    ⬇️ Download AeroLinersSet.grf (latest)
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/v/release/Maicarons/AeroLiners-Set?label=Latest%20version&color=blue" alt="Latest version" />
  <img src="https://img.shields.io/github/downloads/Maicarons/AeroLiners-Set/total?label=Total%20downloads" alt="Total downloads" />
</p>

## Method 1: Download the Release (recommended)

Get the compiled `.grf` from this repository's GitHub Releases. The button above jumps to the **latest** release page automatically; download `AeroLinersSet.grf` there.

You can also go manually:

- 📦 Latest (auto-located): [AeroLiners-Set releases/latest](https://github.com/Maicarons/AeroLiners-Set/releases/latest)
- 🗂 All historical versions: [Releases list](https://github.com/Maicarons/AeroLiners-Set/releases)

After downloading, place it in OpenTTD's `newgrf` directory — see "Install into OpenTTD" below, or [Installation & Usage](/guide/installation).

## Method 2: Via BaNaNaS (stable only, English)

Search for **AeroLiners Set** in OpenTTD's in-game **Content** list and click **Download**. This channel provides the upstream English original and does **not** include the Chinese translation.

## Method 3: Build from source

If you want the latest unreleased changes, or wish to modify models and liveries yourself, compile the `.grf` following [Building from Source](/guide/building).

## Install into OpenTTD

1. Place `AeroLinersSet.grf` into OpenTTD's `newgrf` folder:
   - **Windows**: `Documents/OpenTTD/newgrf`
   - **Other systems**: the `newgrf` folder under OpenTTD's user data directory
2. Open OpenTTD → **NewGRF** → **Add**, select **AeroLiners Set**, and enable it.
3. In the language settings, choose **Simplified Chinese** or **Traditional Chinese** to display the Chinese names.

::: tip
Greyscale is the default greyscale base livery with no airline markings — ideal as a base appearance.
:::

## FAQ

**Q: I downloaded it but don't see Chinese names in-game?**
A: You must switch OpenTTD's language setting to Simplified / Traditional Chinese for the Chinese names to take effect.

**Q: It won't load because the version is too old?**
A: AeroLiners Set requires OpenTTD 1.2.0 or newer (the version with the Chinese interface). Please upgrade OpenTTD and try again.

**Q: Can I use it alongside other aircraft NewGRFs?**
A: Yes, AeroLiners Set does not conflict with other aircraft NewGRFs.

<style>
.download-btn {
  display: inline-block;
  padding: 14px 28px;
  font-size: 1.1rem;
  font-weight: 600;
  color: #fff !important;
  background: #2563eb;
  border-radius: 10px;
  text-decoration: none !important;
  box-shadow: 0 4px 14px rgba(37, 99, 235, 0.35);
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}
.download-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 18px rgba(37, 99, 235, 0.45);
}
</style>
