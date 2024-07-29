from mkdocs.plugins import BasePlugin
from bs4 import BeautifulSoup

class MkdocsExternalLinkProcessor(BasePlugin):
    """
    MkdocsExternalLinkProcessor is a MkDocs plugin that processes HTML content to modify external links.
    
    This plugin adds a specific class to external links, sets the `target` attribute for opening links in a new tab/window,
    and optionally sets the `rel` attribute for those links based on the configuration.

    Attributes:
        class_name (str): The class name to add to external links. Defaults to 'external'.
        target (str): The target attribute value for links, e.g., '_blank' to open links in a new tab. Defaults to an empty string.
        rel (list): The rel attribute value(s) to apply to links. Defaults to an empty list.
        additional_protocols (list): Additional protocols to consider as external. Defaults to an empty list.
        default_protocols (list): The standard list of protocols to consider as external links. Includes 'http://', 'https://', 'ftp://', 'mailto:', 'tel:'.
        all_protocols (list): Combination of default_protocols and additional_protocols.

    Methods:
        on_page_content(html: str, page, config, files) -> str:
            Processes the provided HTML content, modifies external links based on the configuration, and returns the updated HTML content.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the MkdocsExternalLinkProcessor with configuration options.
        
        Args:
            *args: Variable length argument list, passed to the parent class initializer.
            **kwargs: Arbitrary keyword arguments, used to configure the plugin.

        Configurable options:
            - 'class_name': The class name to add to external links (str).
            - 'link_target': The target attribute value for links (str).
            - 'link_rel': The rel attribute value(s) for links (list of str).
            - 'additional_protocols': Additional protocols to consider as external links (list of str).
        """
        super().__init__(*args, **kwargs)
        self.class_name = self.config.get('class_name', 'external')
        self.target = self.config.get('link_target', '')
        self.rel = self.config.get('link_rel', [])
        self.additional_protocols = self.config.get('additional_protocols', [])
        self.default_protocols = ['http://', 'https://', 'ftp://', 'mailto:', 'tel:']
        self.all_protocols = self.default_protocols + self.additional_protocols

    def on_page_content(self, html: str, page, config, files) -> str:
        """
        Processes HTML content to modify external links.

        This method parses the provided HTML, finds all anchor (`<a>`) tags with `href` attributes, and updates them based on
        the plugin's configuration:
        
        - Adds a specified class to external links.
        - Sets the `target` attribute if configured.
        - Sets the `rel` attribute if configured.

        Args:
            html (str): The HTML content of the page.
            page: The MkDocs page object (not used in this method).
            config: The MkDocs configuration object (not used in this method).
            files: The MkDocs files object (not used in this method).

        Returns:
            str: The modified HTML content with updated external links.
        """
        soup = BeautifulSoup(html, 'html.parser')
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if any(href.startswith(protocol) for protocol in self.all_protocols):
                if 'external' not in a_tag.get('class', []):
                    classes = a_tag.get('class', [])
                    if not isinstance(classes, list):
                        classes = []
                    a_tag['class'] = classes + [self.class_name]

            if self.target:
                a_tag["target"] = self.target

            if self.rel:
                a_tag["rel"] = self.rel

        return str(soup)