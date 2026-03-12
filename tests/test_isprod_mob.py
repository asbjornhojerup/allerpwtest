"""Isabellas production tests - mobile"""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_mobile(page: Page):
    """Configure page for mobile viewport."""
    page.set_viewport_size({"width": 390, "height": 844})
    yield page


def test_accept_all_cookies(page_mobile: Page):
    """Test accepting all cookies."""
    page_mobile.goto("https://isabellas.dk/")
    page_mobile.get_by_role("button", name="Tillad alle cookies").click()


def test_open_menu_item_go_to_category(page_mobile: Page):
    """Test opening menu item and navigating to category."""
    page_mobile.goto("https://isabellas.dk/")
    page_mobile.get_by_role("button", name="Tillad alle cookies").click()
    page_mobile.get_by_role("button", name="Menu").click()
    page_mobile.get_by_role("button", name="Udfold menu", exact=True).first.click()
    page_mobile.get_by_role("link", name="Havetips", exact=True).first.click()
    expect(page_mobile.get_by_role("heading", name="Havetips", exact=True)).to_be_visible()


def test_load_more_on_category_page(page_mobile: Page):
    """Test load more functionality on category page."""
    page_mobile.goto("https://isabellas.dk/haven")
    page_mobile.get_by_role("button", name="Tillad alle cookies").click()
    page_mobile.get_by_role("button", name="Hent flere").click()


def test_open_article_on_category_page(page_mobile: Page):
    """Test opening article from category page."""
    page_mobile.goto("https://isabellas.dk/haven")
    page_mobile.get_by_role("button", name="Tillad alle cookies").click()
    page_mobile.locator('//*[@class="max-w-full pt-30 px-30 pb-70 md:pt-20 md:pb-75 flex-grow flex flex-col"]').first.click()
    expect(page_mobile.locator('//div[@class="font-bold tracking-0-6 text-12 leading-18 mb-10 text-center uppercase"]')).to_be_visible()


def test_direct_link_to_article(page_mobile: Page):
    """Test accessing article via direct link."""
    page_mobile.goto(
        "https://isabellas.dk/haven/blomster-planter/6-planter-der-kan-overleve-efteraaret-i-krukker"
    )
    page_mobile.get_by_role("button", name="Tillad alle cookies").click()


def test_video_player_total_consent(page_mobile: Page):
    """Test video player with all cookies allowed."""
    page_mobile.goto(
        "https://isabellas.dk/haven/blomster-planter/6-planter-der-kan-overleve-efteraaret-i-krukker"
    )
    page_mobile.get_by_role("button", name="Tillad alle cookies").click()
    page_mobile.evaluate("window.scrollBy(0, 9000)")
    expect(page_mobile.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_video_player_necessary_consent(page_mobile: Page):
    """Test video player with necessary cookies only."""
    page_mobile.goto(
        "https://isabellas.dk/haven/blomster-planter/6-planter-der-kan-overleve-efteraaret-i-krukker"
    )
    page_mobile.get_by_role("button", name="Kun nødvendige cookies").click()
    page_mobile.evaluate("window.scrollBy(0, 9000)")
    expect(page_mobile.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_ad_placements_on_frontpage(page_mobile: Page):
    """Test ad placements on frontpage."""
    page_mobile.goto("https://isabellas.dk")
    page_mobile.get_by_role("button", name="Tillad alle cookies").click()
    expect(page_mobile.locator("#responsive_1-1")).to_be_visible()


def test_ad_placements_on_article(page_mobile: Page):
    """Test ad placements on article page."""
    page_mobile.goto(
        "https://isabellas.dk/haven/blomster-planter/6-planter-der-kan-overleve-efteraaret-i-krukker"
    )
    page_mobile.get_by_role("button", name="Tillad alle cookies").click()
    expect(page_mobile.locator("#responsive_1-1")).to_be_visible()
