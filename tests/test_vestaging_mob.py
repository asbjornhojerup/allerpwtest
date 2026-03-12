"""Vielskerserier staging tests - mobile"""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_mobile(page: Page):
    """Configure page for mobile viewport."""
    page.set_viewport_size({"width": 390, "height": 844})
    yield page


def test_accept_all_cookies(page_mobile: Page):
    """Test accepting all cookies."""
    page_mobile.goto("https://frontend-stage.vielskerserier.dk/")
    page_mobile.get_by_role("button", name="Tillad alle").click()


def test_open_menu_item_go_to_category(page_mobile: Page):
    """Test opening menu item and navigating to category."""
    page_mobile.goto("https://frontend-stage.vielskerserier.dk/")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.get_by_role("button", name="Menu").click()
    page_mobile.get_by_role("button", name="Udfold menu", exact=True).click()
    page_mobile.get_by_role("link", name="Film", exact=True).first.click()
    expect(page_mobile.get_by_role("heading", name="Film")).to_be_visible()


def test_load_more_on_category_page(page_mobile: Page):
    """Test load more functionality on category page."""
    page_mobile.goto("https://frontend-stage.vielskerserier.dk/film/film-nyheder/")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.get_by_role("button", name="Hent flere").click()


def test_open_article_on_category_page(page_mobile: Page):
    """Test opening article from category page."""
    page_mobile.goto("https://frontend-stage.vielskerserier.dk/film/film-nyheder/")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.locator('//*[@class="col-span-1 mb-25"]').first.click()
    expect(page_mobile.locator('//div[@class="lg:flex items-center justify-center px-10 lg:px-0 mb-20 text-12 lg:text-14 leading-16 text-gray-550 font-medium order-last lg:order-none"]')).to_be_visible()


def test_direct_link_to_article(page_mobile: Page):
    """Test accessing article via direct link."""
    page_mobile.goto(
        "https://frontend-stage.vielskerserier.dk/film/film-nyheder/den-sidste-viking-udtaget-til-prestigefyldt-filmfestival"
    )
    page_mobile.get_by_role("button", name="Tillad alle").click()


def test_video_player_total_consent(page_mobile: Page):
    """Test video player with all cookies allowed."""
    page_mobile.goto(
        "https://frontend-stage.vielskerserier.dk/film/film-nyheder/den-sidste-viking-udtaget-til-prestigefyldt-filmfestival"
    )
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.evaluate("window.scrollBy(0, 1000)")
    expect(page_mobile.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_video_player_necessary_consent(page_mobile: Page):
    """Test video player with necessary cookies only."""
    page_mobile.goto(
        "https://frontend-stage.vielskerserier.dk/film/film-nyheder/den-sidste-viking-udtaget-til-prestigefyldt-filmfestival"
    )
    page_mobile.get_by_role("button", name="Kun nødvendige cookies").click()
    page_mobile.evaluate("window.scrollBy(0, 1000)")
    expect(page_mobile.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_ad_placements_on_frontpage(page_mobile: Page):
    """Test ad placements on frontpage."""
    page_mobile.goto("https://frontend-stage.vielskerserier.dk")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    expect(page_mobile.locator("#responsive_1-1")).to_be_visible()


def test_ad_placements_on_article(page_mobile: Page):
    """Test ad placements on article page."""
    page_mobile.goto(
        "https://frontend-stage.vielskerserier.dk/film/film-anmeldelser/anmeldelse-mr-scorsese-er-et-forrygende-portraet-af-en-levende-filmlegende"
    )
    page_mobile.get_by_role("button", name="Tillad alle").click()
    expect(page_mobile.locator("#responsive_1-1")).to_be_visible()
