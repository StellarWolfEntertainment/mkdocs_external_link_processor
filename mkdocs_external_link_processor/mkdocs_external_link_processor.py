from mkdocs.plugins import BasePlugin
from bs4 import BeautifulSoup

class MkdocsExternalLinkProcessor(BasePlugin):
    """
    A MkDocs plugin that adds a CSS class to external links in the page content.

    This plugin processes the HTML content of MkDocs pages and appends a specified
    class to external links (links starting with 'http://', 'https://', or 'www').

    Attributes:
        class_name (str): The CSS class to add to external links. Defaults to 'external'.
        target (str): The target attribute for external links. Defaults to '_blank'.
        rel (list): The rel attribute for external links. Defaults to ['noopener', 'noreferrer'].
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initializes the plugin and retrieves the CSS class name and attributes from the configuration.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
        self.class_name = self.config.get('external_link_class_name', 'external')
        self.target = self.config.get('link_target', '_blank')
        self.rel = self.config.get('link_rel', ['noopener', 'noreferrer'])

    def on_page_content(self, html: str, page, config, files) -> str:
        """
        Process the HTML content of the page, adding a class to external links.

        This method modifies the HTML content by appending a specified CSS class to
        external links and setting them to open in a new tab with secure attributes.

        Args:
            html (str): The HTML content of the page.
            page (Page): The page object.
            config (MkDocsConfig): The MkDocs configuration dictionary.
            files (Files): The list of files to be processed.

        Returns:
            str: The modified HTML content with the class added to external links,
                 and the links set to open in a new tab with secure attributes.
        """
        soup = BeautifulSoup(html, 'html.parser')
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if not href.startswith(('http://', 'https://', 'www')):
                continue

            if 'external' not in a_tag.get('class', []):
                
                classes = a_tag.get('class', [])
                if not isinstance(classes, list):
                    classes = []
                a_tag['class'] = classes + [self.class_name]
                
            a_tag["target"] = self.target
            a_tag["rel"] = self.rel
        return str(soup)
