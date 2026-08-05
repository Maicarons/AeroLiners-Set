import { defineConfig } from 'vitepress'

const repo = 'Maicarons/AeroLiners-Set'
const site = 'https://maicarons.github.io/AeroLiners-Set/'

export default defineConfig({
  // 部署到 GitHub Pages 项目页（https://<user>.github.io/<repo>/）时，
  // 所有资源/路由必须以仓库名为 base，否则 CSS/JS/图片路径全部 404。
  base: '/AeroLiners-Set/',
  title: 'AeroLiners Set · 寰宇飞机',
  description: 'AeroLiners Set (寰宇飞机) —— 为 OpenTTD 提供的真实世界客机与涂装 NewGRF 项目文档',
  lastUpdated: true,
  cleanUrls: true,

  head: [
    ['link', { rel: 'icon', href: '/logo.png' }],
    // SEO / 社交分享
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:title', content: 'AeroLiners Set (寰宇飞机) 文档' }],
    ['meta', { property: 'og:description', content: '为 OpenTTD 打造的真实世界客机与涂装 NewGRF 项目文档' }],
    ['meta', { property: 'og:site_name', content: 'AeroLiners Set' }],
    ['meta', { property: 'og:locale', content: 'zh_CN' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }]
  ],

  locales: {
    root: {
      label: '简体中文',
      lang: 'zh-CN',
      themeConfig: {
        nav: [
          { text: '首页', link: '/' },
          { text: '机队图鉴', link: '/aircraft/' },
          { text: '指南', link: '/guide/introduction' },
          { text: '构建', link: '/guide/building' },
          { text: '下载', link: '/guide/download' },
          { text: '贡献', link: '/guide/contributing' },
          {
            text: '外部链接',
            items: [
              { text: '文档站', link: site },
              { text: '开发主页 (dev.openttdcoop)', link: 'https://dev.openttdcoop.org/projects/worldairlinersset' },
              { text: '本项目 GitHub 仓库', link: `https://github.com/${repo}` },
              { text: '上游仓库 (RvP93)', link: 'https://github.com/RvP93/WorldAirlinersSet' },
              { text: '许可协议 GPL-3.0', link: '/guide/license' }
            ]
          }
        ],

        sidebar: {
          '/guide/': [
            {
              text: '入门',
              items: [
                { text: '项目简介', link: '/guide/introduction' },
                { text: '安装与使用', link: '/guide/installation' },
                { text: '下载模型', link: '/guide/download' },
                { text: 'NewGRF 参数', link: '/guide/parameters' }
              ]
            },
            {
              text: '开发',
              items: [
                { text: '项目结构', link: '/guide/project-structure' },
                { text: '从源码构建', link: '/guide/building' },
                { text: '涂装与图形', link: '/guide/liveries' },
                { text: '语言翻译', link: '/guide/translating' },
                { text: '占位机型待办', link: '/guide/placeholder-aircraft-todo' }
              ]
            },
            {
              text: '项目信息',
              items: [
                { text: '贡献指南', link: '/guide/contributing' },
                { text: '更新日志', link: '/guide/changelog' },
                { text: '致谢名单', link: '/guide/credits' },
                { text: '许可协议', link: '/guide/license' }
              ]
            }
          ],
          '/aircraft/': [
            { text: '机队图鉴总览', link: '/aircraft/' },
            {
              text: '制造商',
              items: [
                { text: '空中客车 Airbus', link: '/aircraft/airbus' },
                { text: '安东诺夫 Antonov', link: '/aircraft/antonov' },
                { text: 'ATR', link: '/aircraft/atr' },
                { text: 'BAC', link: '/aircraft/bac' },
                { text: 'BAe', link: '/aircraft/bae' },
                { text: '波音 Boeing', link: '/aircraft/boeing' },
                { text: '庞巴迪 Bombardier', link: '/aircraft/bombardier' },
                { text: '巴航工业 Embraer', link: '/aircraft/embraer' },
                { text: '中国商飞 COMAC', link: '/aircraft/comac' },
                { text: '福克 Fokker', link: '/aircraft/fokker' },
                { text: '伊留申 Ilyushin', link: '/aircraft/ilyushin' },
                { text: '洛克希德 Lockheed', link: '/aircraft/lockheed' },
                { text: '麦克唐纳·道格拉斯 McDonnell Douglas', link: '/aircraft/mcdonnell_douglas' },
                { text: 'SUD 宇航', link: '/aircraft/sud' },
                { text: '图波列夫 Tupolev', link: '/aircraft/tupolev' }
              ]
            }
          ]
        },

        editLink: {
          pattern: `https://github.com/${repo}/edit/main/docs/:path`,
          text: '在 GitHub 上编辑此页'
        },

        docFooter: {
          prev: '上一页',
          next: '下一页'
        },

        outline: {
          label: '目录'
        },

        lastUpdatedText: '最后更新',
        darkModeSwitchLabel: '主题',
        sidebarMenuLabel: '菜单',
        returnToTopLabel: '返回顶部',
        langMenuLabel: '多语言'
      }
    },

    en: {
      label: 'English',
      lang: 'en-US',
      link: '/en/',
      themeConfig: {
        nav: [
          { text: 'Home', link: '/' },
          { text: 'Fleet', link: '/aircraft/' },
          { text: 'Guides', link: '/guide/introduction' },
          { text: 'Build', link: '/guide/building' },
          { text: 'Download', link: '/guide/download' },
          { text: 'Contribute', link: '/guide/contributing' },
          {
            text: 'External Links',
            items: [
              { text: 'Docs Site', link: site },
              { text: 'Dev homepage (dev.openttdcoop)', link: 'https://dev.openttdcoop.org/projects/worldairlinersset' },
              { text: 'GitHub Repository', link: `https://github.com/${repo}` },
              { text: 'Upstream (RvP93)', link: 'https://github.com/RvP93/WorldAirlinersSet' },
              { text: 'License GPL-3.0', link: '/guide/license' }
            ]
          }
        ],

        sidebar: {
          '/guide/': [
            {
              text: 'Getting Started',
              items: [
                { text: 'Introduction', link: '/guide/introduction' },
                { text: 'Installation & Usage', link: '/guide/installation' },
                { text: 'Download', link: '/guide/download' },
                { text: 'NewGRF Parameters', link: '/guide/parameters' }
              ]
            },
            {
              text: 'Development',
              items: [
                { text: 'Project Structure', link: '/guide/project-structure' },
                { text: 'Building from Source', link: '/guide/building' },
                { text: 'Liveries & Graphics', link: '/guide/liveries' },
                { text: 'Translating', link: '/guide/translating' },
                { text: 'Placeholder Aircraft TODO', link: '/guide/placeholder-aircraft-todo' }
              ]
            },
            {
              text: 'Project Info',
              items: [
                { text: 'Contributing', link: '/guide/contributing' },
                { text: 'Changelog', link: '/guide/changelog' },
                { text: 'Credits', link: '/guide/credits' },
                { text: 'License', link: '/guide/license' }
              ]
            }
          ],
          '/aircraft/': [
            { text: 'Fleet Overview', link: '/aircraft/' },
            {
              text: 'Manufacturers',
              items: [
                { text: 'Airbus', link: '/aircraft/airbus' },
                { text: 'Antonov', link: '/aircraft/antonov' },
                { text: 'ATR', link: '/aircraft/atr' },
                { text: 'BAC', link: '/aircraft/bac' },
                { text: 'BAe', link: '/aircraft/bae' },
                { text: 'Boeing', link: '/aircraft/boeing' },
                { text: 'Bombardier', link: '/aircraft/bombardier' },
                { text: 'Embraer', link: '/aircraft/embraer' },
                { text: 'COMAC', link: '/aircraft/comac' },
                { text: 'Fokker', link: '/aircraft/fokker' },
                { text: 'Ilyushin', link: '/aircraft/ilyushin' },
                { text: 'Lockheed', link: '/aircraft/lockheed' },
                { text: 'McDonnell Douglas', link: '/aircraft/mcdonnell_douglas' },
                { text: 'SUD Aviation', link: '/aircraft/sud' },
                { text: 'Tupolev', link: '/aircraft/tupolev' }
              ]
            }
          ]
        },

        editLink: {
          pattern: `https://github.com/${repo}/edit/main/docs/:path`,
          text: 'Edit this page on GitHub'
        },

        docFooter: {
          prev: 'Previous',
          next: 'Next'
        },

        outline: {
          label: 'On this page'
        },

        lastUpdatedText: 'Last updated',
        darkModeSwitchLabel: 'Theme',
        sidebarMenuLabel: 'Menu',
        returnToTopLabel: 'Return to top',
        langMenuLabel: 'Languages'
      }
    }
  },

  themeConfig: {
    logo: '/logo.png',

    socialLinks: [
      { icon: 'github', link: `https://github.com/${repo}` }
    ],

    search: {
      provider: 'local'
    }
  }
})
