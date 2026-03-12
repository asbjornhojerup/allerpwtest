"""Vielskerserier staging tests - desktop"""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_desktop(page: Page):
    """Configure page for desktop viewport."""
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page


def test_accept_all_cookies(page_desktop: Page):
    """Test accepting all cookies."""
    page_desktop.goto("https://frontend-stage.vielskerserier.dk/")
    page_desktop.get_by_role("button", name="Tillad alle").click()


def test_open_menu_item_go_to_category(page_desktop: Page):
    """Test opening menu item and navigating to category."""
    page_desktop.goto("https://frontend-stage.vielskerserier.dk/")
    page_desktop.get_by_role("button", name="Tillad alle").click()
    page_desktop.locator("#site-header").get_by_role("link", name="FILM").hover()
    page_desktop.get_by_role("link", name="Nyheder", exact=True).click()
    expect(page_desktop.get_by_role("heading", name="Film | Nyheder")).to_be_visible()


def test_load_more_on_category_page(page_desktop: Page):
    """Test load more functionality on category page."""
    page_desktop.goto("https://frontend-stage.vielskerserier.dk/film/film-nyheder/")
    page_desktop.get_by_role("button", name="Tillad alle").click()
    page_desktop.get_by_role("button", name="Hent flere").click()


def test_open_article_on_category_page(page_desktop: Page):
    """Test opening article from category page."""
    page_desktop.goto("https://frontend-stage.vielskerserier.dk/film/film-nyheder/")
    page_desktop.get_by_role("button", name="Tillad alle").click()
    page_desktop.locator('//*[@class="col-span-1 mb-25"]').first.click()
    expect(page_desktop.locator('//div[@class="lg:flex items-center justify-center px-10 lg:px-0 mb-20 text-12 lg:text-14 leading-16 text-gray-550 font-medium order-last lg:order-none"]')).to_be_visible()


def test_direct_link_to_article(page_desktop: Page):
    """Test accessing article via direct link."""
    page_desktop.goto(
        "https://frontend-stage.vielskerserier.dk/film/film-nyheder/den-sidste-viking-udtaget-til-prestigefyldt-filmfestival"
    )
    page_desktop.get_by_role("button", name="Tillad alle").click()


def test_video_player_total_consent(page_desktop: Page):
    """Test video player with all cookies allowed."""
    page_desktop.goto(
        "https://frontend-stage.vielskerserier.dk/film/film-nyheder/den-sidste-viking-udtaget-til-prestigefyldt-filmfestival"
    )
    page_desktop.get_by_role("button", name="Tillad alle").click()
    page_desktop.evaluate("window.scrollBy(0, 1000)")
    expect(page_desktop.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_video_player_necessary_consent(page_desktop: Page):
    """Test video player with necessary cookies only."""
    page_desktop.goto(
        "https://frontend-stage.vielskerserier.dk/film/film-nyheder/den-sidste-viking-udtaget-til-prestigefyldt-filmfestival"
    )
    page_desktop.get_by_role("button", name="Kun nødvendige cookies").click()
    page_desktop.evaluate("window.scrollBy(0, 1000)")
    expect(page_desktop.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_ad_placements_on_frontpage(page_desktop: Page):
    """Test ad placements on frontpage."""
    page_desktop.goto("https://frontend-stage.vielskerserier.dk")
    page_desktop.get_by_role("button", name="Tillad alle").click()
    expect(page_desktop.locator("#responsive_1-1")).to_be_visible()


def test_ad_placements_on_article(page_desktop: Page):
    """Test ad placements on article page."""
    page_desktop.goto(
        "https://frontend-stage.vielskerserier.dk/film/film-anmeldelser/anmeldelse-cillian-murphy-kan-som-ingen-anden-fortaelle-en-hel-historie-med"
    )
    page_desktop.get_by_role("button", name="Tillad alle").click()
    expect(page_desktop.locator("#responsive_1-1")).to_be_visible()
