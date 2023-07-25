const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    client:{
      webSocketURL: 'auto://gmc.cps.akita-pu.ac.jp/ws',
    },
    proxy: {
      '/login': {
        target: 'https://gmc.cps.akita-pu.ac.jp',
        changeOrigin: true,
        secure: false
      }
    },
  },
  pluginOptions: {
    vuetify: {
      // https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
    }
  }
})
