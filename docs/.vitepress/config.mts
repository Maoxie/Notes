import { defineConfig } from 'vitepress'
import mathjax3 from 'markdown-it-mathjax3';

import structure from '../structure.json';

const customElements = ['mjx-container'];

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Y's Notes",
  description: "My notes collections.",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Examples', link: '/markdown-examples' }
    ],
    sidebar: structure,
    socialLinks: [
      { icon: 'github', link: 'https://github.com/Maoxie/Notes' }
    ]
  },
  base: '/Notes/',
  srcDir: '.',
  markdown: {
    math: true,
    config: (md) => {
      md.use(mathjax3);
    },
  },
  vue: {
    template: {
      compilerOptions: {
        isCustomElement: (tag) => customElements.includes(tag),
      },
    },
  },
})
