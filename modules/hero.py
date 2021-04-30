"""Hero module"""
from models.hero import Hero
import re


class HeroModule(object):
    """Hero module"""

    @staticmethod
    def create(params):
        """
        Create a new hero
        :param dict params: Request dict params
        :return Hero: Hero created
        """
        hero = Hero()
        hero.name = params['name']
        hero.description = params['description']
        hero.imageUrl = params['imageUrl']
        hero.universe = params['universe']
        HeroModule.format_hero_params(hero)
        HeroModule.valid_hero_params(hero)
        HeroModule.valid_url_params(hero)
        hero.save()
        return hero

    @staticmethod
    def update(hero, params):
        """Update hero"""
        hero.name = params['name']
        hero.description = params['description']
        hero.imageUrl = params['imageUrl']
        hero.universe = params['universe']
        HeroModule.format_hero_params(hero)
        HeroModule.valid_hero_params(hero)
        HeroModule.valid_url_params(hero)
        hero.save()

    @staticmethod
    def valid_hero_params(hero):
        """Valid hero params"""
        if not hero.name:
            raise Exception('Bad request, name is required')
        if not hero.universe == 'dc' or hero.universe == 'marvel':
            raise Exception("Bad request, invalid universe")

    @staticmethod
    def format_hero_params(hero):
        """Format hero params"""
        hero.name = hero.name.title().strip()
        if hero.description:
            hero.description = hero.description.title().strip()

    @staticmethod
    def valid_url_params(hero):
        url = hero.imageUrl
        r = re.search("^https?://.", url)
        if not r:
            raise Exception("Bad request, invalid url")

