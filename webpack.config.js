const path = require('path');

module.exports = {
  entry: path.resolve(__dirname, 'leadmanager', 'frontend', 'src', 'index.js'),
  output: {
    path: path.resolve(__dirname, 'leadmanager', 'frontend', 'static', 'frontend'),
    filename: 'main.js',
  },
  resolve: {
    modules: [path.resolve(__dirname, 'leadmanager', 'frontend', 'src'), 'node_modules'],
    extensions: ['.js', '.json'],
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
    ],
  },
};
