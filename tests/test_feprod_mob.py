"""Femina production tests - mobile"""
import pytest
from playwright.sync_api import Page, expect


@pytest.fixture
def page_mobile(page: Page):
    """Configure page for mobile viewport."""
    page.set_viewport_size({"width": 390, "height": 844})
    yield page


def test_open_menu_go_to_category(page_mobile: Page):
    """Test opening menu and navigating to category."""
    page_mobile.goto("https://femina.dk/")
    page_mobile.get_by_role("button", name="Tillad alle cookies").click()
    page_mobile.get_by_role("button", name="Menu").click()
    page_mobile.get_by_role("link", name="Agenda", exact=True).click()


def test_go_to_frontpage_by_clicking_logo(page_mobile: Page):
    """Test returning to frontpage via logo."""
    page_mobile.goto("https://femina.dk/agenda")
    page_mobile.get_by_role("button", name="Tillad alle cookies").click()
    page_mobile.get_by_label("Gå til forsiden").click()


def test_load_more_on_category_page(page_mobile: Page):
    """Test load more functionality on category page."""
    page_mobile.goto("https://femina.dk/agenda")
    page_mobile.get_by_role("button", name="Tillad alle cookies").click()
    page_mobile.evaluate("window.scrollBy(0, 1000)")
    page_mobile.get_by_role("button", name="Hent flere").click()


def test_open_article_on_category_page(page_mobile: Page):
    """Test opening article from category page."""
    page_mobile.goto("https://femina.dk/agenda")
    page_mobile.get_by_role("button", name="Tillad alle cookies").click()
    page_mobile.locator('//*[@class="flex-grow relative mb-40 lg:mb-50 bg-sand-400 col-span-12 lg:col-span-3"]').first.click()
    expect(page_mobile.locator('//*[@class="font-serif text-20 leading-26 py-20 max-w-710 md:text-24 md:leading-32 lg:text-24 lg:leading-34"]')).to_be_visible()


def test_video_player_total_consent(page_mobile: Page):
    """Test video player with all cookies allowed."""
    page_mobile.goto(
        "https://femina.dk/agenda/karriere-og-penge/kendt-radiovaert-erstatter-sofie-linde-som-x-factor-vaert"
    )
    page_mobile.get_by_role("button", name="Tillad alle cookies").click()
    page_mobile.evaluate("window.scrollBy(0, 1000)")
    expect(page_mobile.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_video_player_necessary_consent(page_mobile: Page):
    """Test video player with necessary cookies only."""
    page_mobile.goto(
        "https://femina.dk/agenda/karriere-og-penge/kendt-radiovaert-erstatter-sofie-linde-som-x-factor-vaert"
    )
    page_mobile.get_by_role("button", name="Kun nødvendige cookies").click()
    page_mobile.evaluate("window.scrollBy(0, 1000)")
    expect(page_mobile.locator('//div[@class="jw-media jw-reset"]')).to_be_visible()


def test_newsletter_signup(page_mobile: Page):
    """Test newsletter signup form."""
    page_mobile.goto("https://femina.dk/nyhedsbrev")
    page_mobile.get_by_role("button", name="Tillad alle cookies").click()
    page_mobile.locator('//input[@id="email"]').fill("jjk@mailinator.com")
    page_mobile.locator('//input[@id="firstname"]').fill("Jens")
    page_mobile.locator('//input[@id="lastname"]').fill("Jensen")
    page_mobile.locator('//input[@id="postal"]').fill("4070")
    page_mobile.locator('//input[@id="terms"]').click()
    page_mobile.locator('//button[@type="submit"]').click()
    expect(page_mobile.get_by_text("Tak for tilmeldingen")).to_be_visible()


def test_sign_in_to_plus(page_mobile: Page):
    """Test signing in to plus subscription."""
    page_mobile.goto("https://femina.dk/plus")
    page_mobile.get_by_role("button", name="Tillad alle cookies").click()
    page_mobile.locator('//input[@id="email"]').fill("asbjornsjunk@gmail.com")
    page_mobile.locator('//input[@id="password"]').fill("Gyg37cnr")
    page_mobile.locator('//button[@type="submit"]').click()
    expect(page_mobile.get_by_role("link", name="Indstillinger", exact=True)).to_be_visible()


def test_ad_placements_on_frontpage(page_mobile: Page):
    """Test ad placements on frontpage."""
    page_mobile.goto("https://femina.dk")
    page_mobile.get_by_role("button", name="Tillad alle cookies").click()
    expect(page_mobile.locator("#responsive_1-1")).to_be_visible()


def test_ad_placements_on_article(page_mobile: Page):
    """Test ad placements on article page."""
    page_mobile.goto(
        "https://femina.dk/sundhed/jeg-er-paa-vej-hjem-til-dig-nu-sagde-vagtlaegen-i-telefonen-ingen-havde-regnet-med-noget"
    )
    page_mobile.get_by_role("button", name="Tillad alle cookies").click()
    expect(page_mobile.locator("#responsive_1-1")).to_be_visible()
