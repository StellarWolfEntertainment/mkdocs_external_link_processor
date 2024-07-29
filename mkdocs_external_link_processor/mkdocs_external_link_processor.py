from mkdocs.plugins import BasePlugin
from bs4 import BeautifulSoup

class MkdocsExternalLinkProcessor(BasePlugin):
    """
    A MkDocs plugin that adds a CSS class to external links in the page content.

    This plugin processes the HTML content of MkDocs pages and appends a specified
    class to external links (links starting with 'http://' or 'https://').

    Attributes:
        class_name (str): The CSS class to add to external links. Defaults to 'external'.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the plugin and retrieves the CSS class name from the configuration.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.class_name = self.config.get('external_link_class_name', 'external')

    def on_page_content(self, html: str, page, config, files) -> str:
        """
        Process the HTML content of the page, adding a class to external links.

        Args:
            html (str): The HTML content of the page.
            page (Page): The page object.
            config (MkDocsConfig): The MkDocs configuration dictionary.
            files (Files): The list of files to be processed.

        Returns:
            str: The modified HTML content with the class added to external links.
        """
        soup = BeautifulSoup(html, 'html.parser')
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if href.startswith(('http://', 'https://')):
                if 'external' not in a_tag.get('class', []):
                    
                    classes = a_tag.get('class', [])
                    if not isinstance(classes, list):
                        classes = []
                    a_tag['class'] = classes + [self.class_name]

                a_tag['target']= '_blank'
                a_tag['rel'] = 'noopener noreferrer'
        return str(soup)