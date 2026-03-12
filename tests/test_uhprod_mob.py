"""Udeoghjemme production tests - mobile"""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_mobile(page: Page):
    """Configure page for mobile viewport."""
    page.set_viewport_size({"width": 390, "height": 844})
    yield page


def test_accept_all_cookies(page_mobile: Page):
    """Test accepting all cookies."""
    page_mobile.goto("https://udeoghjemme.dk/")
    page_mobile.get_by_role("button", name="Tillad alle").click()


def test_open_menu_item_go_to_category(page_mobile: Page):
    """Test opening menu item and navigating to category."""
    page_mobile.goto("https://udeoghjemme.dk/")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.get_by_role("button", name="Menu").click()
    page_mobile.locator("#header-main").get_by_role("link", name="Skæbner").first.click()
    expect(page_mobile.get_by_role("heading", name="Skæbner")).to_be_visible()


def test_load_more_on_category_page(page_mobile: Page):
    """Test load more functionality on category page."""
    page_mobile.goto("https://udeoghjemme.dk/skaebner")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.get_by_role("button", name="Hent flere").click()


def test_open_article_on_category_page(page_mobile: Page):
    """Test opening article from category page."""
    page_mobile.goto("https://udeoghjemme.dk/skaebner")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.locator('//div[@class="min-w-[fit-content]"]').first.click()
    expect(page_mobile.locator('//div[@class="mb-30 md:mb-20 mx-20 text-20 leading-26 text-black font-light font-condensed lg:text-24 lg:leading-30"]')).to_be_visible()


def test_newsletter_signup(page_mobile: Page):
    """Test newsletter signup form."""
    page_mobile.goto("https://udeoghjemme.dk/nyhedsbrev")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.locator('//input[@id="edit-email"]').fill("jjk@mailinator.com")
    page_mobile.locator('//input[@id="edit-first-name"]').fill("Jens")
    page_mobile.locator('//input[@id="edit-last-name"]').fill("Jensen")
    page_mobile.locator('//input[@id="edit-phone-number"]').fill("40704070")
    page_mobile.locator('//input[@id="edit-zip-code"]').fill("4070")
    page_mobile.locator('//input[@id="edit-agree"]').click()
    page_mobile.locator('//button[@type="submit"]').click()


def test_direct_link_to_article(page_mobile: Page):
    """Test accessing article via direct link."""
    page_mobile.goto(
        "https://udeoghjemme.dk/reality/love-island/love-island-deltageren-jamie-eschen-skal-i-faengsel-igen-hun-kunne-ikke-faa"
    )
    page_mobile.get_by_role("button", name="Tillad alle").click()


def test_video_player_total_consent(page_mobile: Page):
    """Test video player with all cookies allowed."""
    page_mobile.goto(
        "https://udeoghjemme.dk/skaebner/naar-livet-goer-ondt/marlene-fik-sin-elskede-john-viet-paa-hans-doedsleje"
    )
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.evaluate("window.scrollBy(0, 1000)")
    expect(page_mobile.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_video_player_necessary_consent(page_mobile: Page):
    """Test video player with necessary cookies only."""
    page_mobile.goto(
        "https://udeoghjemme.dk/skaebner/naar-livet-goer-ondt/marlene-fik-sin-elskede-john-viet-paa-hans-doedsleje"
    )
    page_mobile.get_by_role("button", name="Kun nødvendige cookies").click()
    page_mobile.evaluate("window.scrollBy(0, 1000)")
    expect(page_mobile.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_load_more_category_change_consent(page_mobile: Page):
    """Test load more with consent change."""
    page_mobile.goto("https://udeoghjemme.dk/skaebner")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    page_mobile.get_by_role("button", name="Hent flere").click()
    page_mobile.get_by_role("button", name="Administrer samtykke").click()
    page_mobile.get_by_role("button", name="Kun nødvendige cookies").click()
    page_mobile.get_by_role("button", name="Hent flere").click()


def test_ad_placements_on_frontpage(page_mobile: Page):
    """Test ad placements on frontpage."""
    page_mobile.goto("https://udeoghjemme.dk")
    page_mobile.get_by_role("button", name="Tillad alle").click()
    expect(page_mobile.locator("#responsive_1-1")).to_be_visible()


def test_ad_placements_on_article(page_mobile: Page):
    """Test ad placements on article page."""
    page_mobile.goto(
        "https://udeoghjemme.dk/skaebner/naar-livet-goer-ondt/123-omkom-da-olieplatform-kaentrede-anders-sprang-i-havet-og"
    )
    page_mobile.get_by_role("button", name="Tillad alle").click()
    expect(page_mobile.locator("#responsive_1-1")).to_be_visible()
