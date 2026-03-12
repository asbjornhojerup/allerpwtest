"""Femina production tests - desktop"""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_desktop(page: Page):
    """Configure page for desktop viewport."""
    page.set_viewport_size({"width": 1920, "height": 1080})
    yield page


def test_open_menu_go_to_category(page_desktop: Page):
    """Test opening menu and navigating to category."""
    page_desktop.goto("https://femina.dk/")
    page_desktop.get_by_role("button", name="Tillad alle cookies").click()
    page_desktop.get_by_role("button", name="Menu").click()
    page_desktop.get_by_role("link", name="Stil", exact=True).click()


def test_go_to_frontpage_by_clicking_logo(page_desktop: Page):
    """Test returning to frontpage via logo."""
    page_desktop.goto("https://femina.dk/agenda")
    page_desktop.get_by_role("button", name="Tillad alle cookies").click()
    page_desktop.get_by_label("Gå til forsiden").click()


def test_load_more_on_category_page(page_desktop: Page):
    """Test load more functionality on category page."""
    page_desktop.goto("https://femina.dk/agenda")
    page_desktop.get_by_role("button", name="Tillad alle cookies").click()
    page_desktop.evaluate("window.scrollBy(0, 1000)")
    page_desktop.get_by_role("button", name="Hent flere").click()


def test_open_article_on_category_page(page_desktop: Page):
    """Test opening article from category page."""
    page_desktop.goto("https://femina.dk/agenda")
    page_desktop.get_by_role("button", name="Tillad alle cookies").click()
    page_desktop.locator('//*[@class="flex-grow relative mb-40 lg:mb-50 bg-sand-400 col-span-12 lg:col-span-3"]').first.click()
    expect(page_desktop.locator('//*[@class="font-serif text-20 leading-26 py-20 max-w-710 md:text-24 md:leading-32 lg:text-24 lg:leading-34"]')).to_be_visible()


def test_video_player_total_consent(page_desktop: Page):
    """Test video player with all cookies allowed."""
    page_desktop.goto(
        "https://femina.dk/agenda/karriere-og-penge/kendt-radiovaert-erstatter-sofie-linde-som-x-factor-vaert"
    )
    page_desktop.get_by_role("button", name="Tillad alle cookies").click()
    page_desktop.evaluate("window.scrollBy(0, 1000)")
    expect(page_desktop.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_video_player_necessary_consent(page_desktop: Page):
    """Test video player with necessary cookies only."""
    page_desktop.goto(
        "https://femina.dk/agenda/karriere-og-penge/kendt-radiovaert-erstatter-sofie-linde-som-x-factor-vaert"
    )
    page_desktop.get_by_role("button", name="Kun nødvendige cookies").click()
    page_desktop.evaluate("window.scrollBy(0, 1000)")
    expect(page_desktop.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_newsletter_signup(page_desktop: Page):
    """Test newsletter signup form."""
    page_desktop.goto("https://femina.dk/nyhedsbrev")
    page_desktop.get_by_role("button", name="Tillad alle cookies").click()
    page_desktop.locator('//input[@id="email"]').fill("jjk@mailinator.com")
    page_desktop.locator('//input[@id="firstname"]').fill("Jens")
    page_desktop.locator('//input[@id="lastname"]').fill("Jensen")
    page_desktop.locator('//input[@id="postal"]').fill("4070")
    page_desktop.locator('//input[@id="terms"]').click()
    page_desktop.locator('//button[@type="submit"]').click()
    expect(page_desktop.get_by_text("Tak for tilmeldingen")).to_be_visible()


def test_sign_in_to_plus(page_desktop: Page):
    """Test signing in to plus subscription."""
    page_desktop.goto("https://femina.dk/plus")
    page_desktop.get_by_role("button", name="Tillad alle cookies").click()
    page_desktop.locator('//input[@id="email"]').fill("asbjornsjunk@gmail.com")
    page_desktop.locator('//input[@id="password"]').fill("Gyg37cnr")
    page_desktop.locator('//button[@type="submit"]').click()
    expect(page_desktop.get_by_role("link", name="Indstillinger", exact=True)).to_be_visible()


def test_ad_placements_on_frontpage(page_desktop: Page):
    """Test ad placements on frontpage."""
    page_desktop.goto("https://femina.dk")
    page_desktop.get_by_role("button", name="Tillad alle cookies").click()
    expect(page_desktop.locator("#responsive_1-1")).to_be_visible()


def test_ad_placements_on_article(page_desktop: Page):
    """Test ad placements on article page."""
    page_desktop.goto(
        "https://femina.dk/sundhed/jeg-er-paa-vej-hjem-til-dig-nu-sagde-vagtlaegen-i-telefonen-ingen-havde-regnet-med-noget"
    )
    page_desktop.get_by_role("button", name="Tillad alle cookies").click()
    expect(page_desktop.locator("#responsive_1-1")).to_be_visible()
