# MkDocs External Link Processor

A MkDocs plugin that adds a CSS class to external links in your documentation.

## Features

- Automatically adds a specified CSS class to external links (links starting with `http://` or `https://`).
- Configurable class name for external links.
- Adds `target="_blank"` and `rel="noopener noreferrer"` to external links for improved security.

## Installation

You can install the plugin via pip:

```bash
pip install mkdocs-external-link-processor
```

## Usage

Add the plugin to your mkdocs.yml configuration file:

```yaml
plugins:
  - mkdocs_external_link_processor:
      external_link_class_name: 'external'  # Optional: default is 'external'
```

## Configuration

`external_link_class_name`: The CSS class to add to external links. Default is external.

## Example

If you have a link like this:

```html
<a href="https://example.com">Example</a>
```

It will be transformed to:

```html
<a href="https://example.com" class="external" target="_blank" rel="noopener noreferrer">Example</a>
```

## Development

To contribute to the development of this plugin, clone the repository and install the development dependencies:

```bash
git clone https://github.com/StellarWolfEntertainment/mkdocs-external-link-processor.git
cd mkdocs-external-link-processor
pip install -e .
```

## License

This project is licensed under the (MIT License)[LICENSE.md]

## Author

(Raistlin Wolfe)[mailto:jdoonan61@gmail.com?subject=mkdocs_external_link_processor]