import { test, expect } from '@playwright/test';
test.use({ viewport: { width: 1920, height: 1080 } });

test('test open menu, go to category', async ({ page }) => {
  await page.goto('https://billedbladet.dk/');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.getByLabel('Åben menu').click();
  await page.getByRole('link', { name: 'Kendte', exact: true }).click();
});


test('test go to frontpage by clicking logo', async ({ page }) => {
  await page.goto('https://billedbladet.dk/kendte');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.getByRole('link', { name: 'Gå til forsiden' }).click();
});

test('test load more  on category page', async ({ page }) => {
  await page.goto('https://billedbladet.dk/kendte');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.getByRole('button', { name: 'Hent flere' }).click();
});

test('test open article on category page', async ({ page }) => {
  await page.goto('https://billedbladet.dk/kendte');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.locator('//*[@class="rounded-t-10 bg-gray-100 bg-opacity-50"]').click();
  await expect(page.getByRole('heading', { name: "Mest Læste" })).toBeVisible();
});

test('test newsletter sign-up', async ({ page }) => {
  await page.goto('https://billedbladet.dk/nyhedsbrev');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.locator('//input[@id="email"]').fill('jjk@mailinator.com');
  await page.locator('//input[@id="firstname"]').fill('Jens');
  await page.locator('//input[@id="postalcode"]').fill('4070');
  await page.locator('//input[@id="terms"]').click();
  await page.locator('//button[@type="submit"]').click();
});

test('direct link to article', async ({ page }) => {
  await page.goto('https://billedbladet.dk/nostalgi/husker-du-da-benedikte-og-anne-marie-forstyrrede-fars-nytaarstale');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
});

//tests if jw player is loaded after marketing consent is given
test('test video player, total consent', async ({ page }) => {
  await page.goto('https://www.billedbladet.dk/kongelige/danmark/prinsesse-josephine-og-prins-vincents-glamouroese-look-glimtende-stene-og-james');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.evaluate(() => { 
    window.scrollBy(0, 1000);
  });
  await expect(page.locator('//div[@class="jw-media jw-reset"]')).toBeVisible();
});


//tests if jw player is hidden on use of necessary consent
test('test video player, necessary consent', async ({ page }) => {
  await page.goto('https://www.billedbladet.dk/kongelige/danmark/prinsesse-josephine-og-prins-vincents-glamouroese-look-glimtende-stene-og-james');
  await page.getByRole('button', { name: 'Use necessary cookies only' }).click();
  await page.evaluate(() => { 
    window.scrollBy(0, 1000);
  });
  await expect(page.locator('//div[@class="jw-media jw-reset"]')).toBeVisible();
});

test('test load more  on category , change to necessary cookies, load more again', async ({ page }) => {
  await page.goto('https://billedbladet.dk/kendte');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.getByRole('button', { name: 'Hent flere' }).click();
  await page.getByRole('button', { name: 'Administrer samtykke' }).click();
  await page.getByRole('button', { name: 'Use Necessary cookies' }).click();
  await page.getByRole('button', { name: 'Hent flere' }).click();
});

test('test ad placements on frontpage', async ({ page }) => {
  await page.goto('https://billedbladet.dk');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await expect(page.locator('#responsive_1-1')).toBeVisible();
});

test('test ad placements on article', async ({ page }) => {
  await page.goto('https://billedbladet.dk/kongelige/danmark/se-videoen-her-ankommer-kongeparret-til-nytaarskur');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await expect(page.locator('#responsive_1-1')).toBeVisible();
});