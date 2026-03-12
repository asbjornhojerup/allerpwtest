"""Isabellas staging tests - desktop"""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_desktop(page: Page):
    """Configure page for desktop viewport."""
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page


def test_accept_all_cookies(page_desktop: Page):
    """Test accepting all cookies."""
    page_desktop.goto("https://frontend-stage.isabellas.dk/")
    page_desktop.get_by_role("button", name="Tillad alle cookies").click()


def test_open_menu_item_go_to_category(page_desktop: Page):
    """Test opening menu item and navigating to category."""
    page_desktop.goto("https://frontend-stage.isabellas.dk/")
    page_desktop.get_by_role("button", name="Tillad alle cookies").click()
    page_desktop.get_by_role("link", name="Have").first.hover()
    page_desktop.get_by_role("link", name="Havetips", exact=True).first.click()
    expect(page_desktop.get_by_role("heading", name="Havetips", exact=True)).to_be_visible()


def test_load_more_on_category_page(page_desktop: Page):
    """Test load more functionality on category page."""
    page_desktop.goto("https://frontend-stage.isabellas.dk/haven")
    page_desktop.get_by_role("button", name="Tillad alle cookies").click()
    page_desktop.get_by_role("button", name="Hent flere").click()


def test_open_article_on_category_page(page_desktop: Page):
    """Test opening article from category page."""
    page_desktop.goto("https://frontend-stage.isabellas.dk/haven")
    page_desktop.get_by_role("button", name="Tillad alle cookies").click()
    page_desktop.locator('//*[@class="max-w-full pt-30 px-30 pb-70 md:pt-20 md:pb-75 flex-grow flex flex-col"]').first.click()
    expect(page_desktop.locator('//div[@class="font-bold tracking-0-6 text-12 leading-18 mb-10 text-center uppercase"]')).to_be_visible()


def test_direct_link_to_article(page_desktop: Page):
    """Test accessing article via direct link."""
    page_desktop.goto(
        "https://frontend-stage.isabellas.dk/haven/blomster-planter/6-planter-der-kan-overleve-efteraaret-i-krukker-0"
    )
    page_desktop.get_by_role("button", name="Tillad alle cookies").click()


def test_video_player_total_consent(page_desktop: Page):
    """Test video player with all cookies allowed."""
    page_desktop.goto(
        "https://frontend-stage.isabellas.dk/haven/blomster-planter/6-planter-der-kan-overleve-efteraaret-i-krukker-0"
    )
    page_desktop.get_by_role("button", name="Tillad alle cookies").click()
    page_desktop.evaluate("window.scrollBy(0, 9000)")
    expect(page_desktop.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_video_player_necessary_consent(page_desktop: Page):
    """Test video player with necessary cookies only."""
    page_desktop.goto(
        "https://frontend-stage.isabellas.dk/haven/blomster-planter/6-planter-der-kan-overleve-efteraaret-i-krukker-0"
    )
    page_desktop.get_by_role("button", name="Kun nødvendige cookies").click()
    page_desktop.evaluate("window.scrollBy(0, 9000)")
    expect(page_desktop.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_ad_placements_on_frontpage(page_desktop: Page):
    """Test ad placements on frontpage."""
    page_desktop.goto("https://frontend-stage.isabellas.dk")
    page_desktop.get_by_role("button", name="Tillad alle cookies").click()
    expect(page_desktop.locator("#responsive_1-1")).to_be_visible()


def test_ad_placements_on_article(page_desktop: Page):
    """Test ad placements on article page."""
    page_desktop.goto(
        "https://frontend-stage.isabellas.dk/haven/blomster-planter/6-planter-der-kan-overleve-efteraaret-i-krukker-0"
    )
    page_desktop.get_by_role("button", name="Tillad alle cookies").click()
    expect(page_desktop.locator("#responsive_1-1")).to_be_visible()
