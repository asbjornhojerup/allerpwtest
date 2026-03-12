"""Seoghoer staging tests - desktop"""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_desktop(page: Page):
    """Configure page for desktop viewport."""
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page


def test_accept_all_cookies(page_desktop: Page):
    """Test accepting all cookies."""
    page_desktop.goto("https://frontend-stage.seoghoer.dk/")
    page_desktop.get_by_role("button", name="Tillad alle").click()


def test_open_menu_go_to_category(page_desktop: Page):
    """Test opening menu and navigating to category."""
    page_desktop.goto("https://frontend-stage.seoghoer.dk/")
    page_desktop.get_by_role("button", name="Tillad alle").click()
    page_desktop.get_by_label("menu").click()
    page_desktop.get_by_role("link", name="Kendte").click()


def test_go_to_frontpage_by_clicking_logo(page_desktop: Page):
    """Test returning to frontpage via logo."""
    page_desktop.goto("https://frontend-stage.seoghoer.dk/kendte")
    page_desktop.get_by_role("button", name="Tillad alle").click()
    page_desktop.locator('//div[contains(@class ,"-mb-5 mr-auto transition-dimensions duration-500 h-80")]').click()


def test_load_more_on_category_page(page_desktop: Page):
    """Test load more functionality on category page."""
    page_desktop.goto("https://frontend-stage.seoghoer.dk/kendte")
    page_desktop.get_by_role("button", name="Tillad alle").click()
    page_desktop.get_by_role("button", name="Hent flere").click()


def test_open_article_on_category_page(page_desktop: Page):
    """Test opening article from category page."""
    page_desktop.goto("https://frontend-stage.seoghoer.dk/kongelige")
    page_desktop.get_by_role("button", name="Tillad alle").click()
    page_desktop.locator('//div[contains(@class ,"mb-5 lg:mb-10 flex items-center justify-center justify-center")]').hover()
    page_desktop.locator('//div[contains(@class ,"mb-5 lg:mb-10 flex items-center justify-center justify-center")]').click()
    page_desktop.evaluate("window.scrollBy(0, 1000)")
    expect(page_desktop.locator('//div[@class="text-20 leading-26 font-bold mb-20"]')).to_be_visible()


def test_newsletter_signup(page_desktop: Page):
    """Test newsletter signup form."""
    page_desktop.goto("https://frontend-stage.seoghoer.dk/nyhedsbrev")
    page_desktop.get_by_role("button", name="Tillad alle").click()
    page_desktop.locator('//input[@id="email"]').fill("jjk@mailinator.com")
    page_desktop.locator('//input[@id="firstname"]').fill("Jens")
    page_desktop.locator('//input[@id="postal"]').fill("4070")
    page_desktop.locator('//input[@id="terms"]').click()
    page_desktop.locator('//button[@type="submit"]').click()


def test_direct_link_to_article(page_desktop: Page):
    """Test accessing article via direct link."""
    page_desktop.goto(
        "https://frontend-stage.seoghoer.dk/reality/love-island/love-island-deltageren-jamie-eschen-skal-i-faengsel-igen-hun-kunne-ikke-faa"
    )
    page_desktop.get_by_role("button", name="Tillad alle").click()


def test_video_player_total_consent(page_desktop: Page):
    """Test video player with all cookies allowed."""
    page_desktop.goto(
        "https://frontend-stage.seoghoer.dk/reality/paradise-hotel/voldsom-video-nadja-hansen-i-dramatisk-ormeulykke-paa-paradise-hotel"
    )
    page_desktop.get_by_role("button", name="Tillad alle").click()
    page_desktop.evaluate("window.scrollBy(0, 1000)")
    expect(page_desktop.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_video_player_necessary_consent(page_desktop: Page):
    """Test video player with necessary cookies only."""
    page_desktop.goto(
        "https://frontend-stage.seoghoer.dk/reality/paradise-hotel/voldsom-video-nadja-hansen-i-dramatisk-ormeulykke-paa-paradise-hotel"
    )
    page_desktop.get_by_role("button", name="Kun nødvendige cookies").click()
    page_desktop.evaluate("window.scrollBy(0, 1000)")
    expect(page_desktop.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_load_more_category_change_consent(page_desktop: Page):
    """Test load more with consent change."""
    page_desktop.goto("https://frontend-stage.seoghoer.dk/kendte")
    page_desktop.get_by_role("button", name="Tillad alle").click()
    page_desktop.get_by_role("button", name="Hent flere").click()
    page_desktop.get_by_role("button", name="Administrer samtykke").click()
    page_desktop.get_by_role("button", name="Kun nødvendige cookies").click()
    page_desktop.get_by_role("button", name="Hent flere").click()


def test_ad_placements_on_frontpage(page_desktop: Page):
    """Test ad placements on frontpage."""
    page_desktop.goto("https://frontend-stage.seoghoer.dk?debugAds=true")
    page_desktop.get_by_role("button", name="Tillad alle").click()
    expect(page_desktop.locator("#responsive_1-1")).to_be_visible()


def test_ad_placements_on_article(page_desktop: Page):
    """Test ad placements on article page."""
    page_desktop.goto(
        "https://frontend-stage.seoghoer.dk/reality/paradise-hotel/voldsom-video-nadja-hansen-i-dramatisk-ormeulykke-paa-paradise-hotel?debugAds=true"
    )
    page_desktop.get_by_role("button", name="Tillad alle").click()
    expect(page_desktop.locator("#responsive_1-1")).to_be_visible()
