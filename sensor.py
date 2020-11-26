from homeassistant.helpers.entity import Entity

import AdvancedHTMLParser
import urllib.request
import requests






def setup_platform(hass, config, add_entities, discovery_info=None):
    add_entities([ReigateBinsSensor()])


class ReigateBinsSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Reigate Bins'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        url = "https://apps.reigate-banstead.gov.uk/Calendar/Controller?uprn=000068102704"
        r = requests.get(url)

        parser = AdvancedHTMLParser.AdvancedHTMLParser()
        parser.parseStr(r.text)

        tomorrow = parser.getElementsByClassName('today')[0].nextElementSibling

        bins = []

        if tomorrow.hasClass('has-collection'):
            print("Has collection tomorrow")
            imgs = parser.getElementsByTagName('img', tomorrow)
            for img in imgs:
                src = img.src.replace("images/rbbc_", "")
                src= src.replace(".jpg", "")
                src= src.replace(".png", "")
                bins.append(src)
                print(src)

        put_out_bins = set(bins)
        self._state =  '_'.join(put_out_bins);
