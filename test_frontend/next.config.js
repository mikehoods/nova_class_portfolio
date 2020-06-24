const withPlugins = require('next-compose-plugins')
const webpack = require('webpack')
const path = require('path')

module.exports = withPlugins([], {
    webpack(config, options){
        config.resolve.modules.push(path.resolve("./"))
        return config
    }
})