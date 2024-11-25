module.exports = {
  chainWebpack: (config) => {
    config.plugin('define').tap((args) => {
      const definitions = args[0]['process.env'];
      Object.assign(definitions, {
        __VUE_OPTIONS_API__: JSON.stringify(true),
        __VUE_PROD_DEVTOOLS__: JSON.stringify(false),
        __VUE_PROD_HYDRATION_MISMATCH_DETAILS__: JSON.stringify(false),
      });
      return args;
    });
  },
};

