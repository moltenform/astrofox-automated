const path = require('path');
const CopyPlugin = require('copy-webpack-plugin');
const TerserPlugin = require('terser-webpack-plugin');

const PRODUCTION = process.env.NODE_ENV === 'production';

module.exports = {
  mode: PRODUCTION ? 'production' : 'development',
  devtool: PRODUCTION ? false : 'source-map',
  target: 'electron-main',
  node: {
    __dirname: false,
    __filename: false,
  },
  entry: {
    main: path.resolve(__dirname, 'src/main/index.js'),
  },
  output: {
    path: path.resolve(__dirname, 'app'),
    filename: '[name].js',
  },
  resolve: {
    extensions: ['.js', '.json'],
    modules: [path.resolve(__dirname, 'src'), 'node_modules'],
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        include: [path.resolve(__dirname, 'src/js')],
        use: [{
          loader: 'babel-loader',
          options: {
            cacheDirectory: true,
          },
        }],
      },
    ],
  },
  plugins: [
    new CopyPlugin({
      patterns: [
        {
          from: path.resolve(__dirname, 'src/build/app'),
          to: path.resolve(__dirname, 'app'),
        },
      ],
    }),
  ],
  optimization: {
    minimize: PRODUCTION,
    minimizer: [
      new TerserPlugin({
        terserOptions: {
          output: {
            comments: false,
          },
        },
        extractComments: false,
      }),
    ],
  },
};
