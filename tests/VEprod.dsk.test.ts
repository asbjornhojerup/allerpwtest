import { test, expect } from '@playwright/test';
test.use({ viewport: { width: 1920, height: 1080 } });

test('test accept all cookies', async ({ page }) => {
    await page.goto('https://vielskerserier.dk/');
    await page.getByRole('button', { name: 'Allow all cookies' }).click();
  });

test('test open menu item, go to category', async ({ page }) => {
  await page.goto('https://vielskerserier.dk/');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.locator('#site-header').getByRole('link', { name: 'FILM' }).hover();
  await page.getByRole('link', { name: 'Nyheder', exact: true }).click();
  {timeout: 30000}
  await expect(page.getByRole('heading', { name: 'Film | Nyheder' })).toBeVisible();
});


test('test load more  on category page', async ({ page }) => {
  await page.goto('https://vielskerserier.dk/film/film-nyheder/');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.getByRole('button', { name: 'Hent flere' }).click();
});

test('test open article on category page', async ({ page }) => {
  await page.goto('https://vielskerserier.dk/film/film-nyheder/');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.locator('//*[@class="col-span-1 mb-25"]').first().click();
  await expect(page.locator('//div[@class="lg:flex items-center justify-center px-10 lg:px-0 mb-20 text-12 lg:text-14 leading-16 text-gray-550 font-medium order-last lg:order-none"]')).toBeVisible();
});


//test('test newsletter sign-up', async ({ page }) => {
  //await page.goto('https://vielskerserier.dk/nyhedsbrev');
  //await page.getByRole('button', { name: 'Allow all cookies' }).click();
  //await page.locator('//input[@id="E-mail *"]').fill('jjk@mailinator.com');
  //await page.locator('//input[@id="fornavn"]').fill('Jens');
  //await page.locator('//input[@id="edit-last-name"]').fill('Jensen');
  //await page.locator('//input[@id="edit-phone-number"]').fill('40704070');
  //await page.locator('//input[@id="edit-zip-code"]').fill('4070');
  //await page.locator('//input[@id="edit-agree"]').click();
  //await page.locator('//button[@type="submit"]').click();
//});

test('direct link to article', async ({ page }) => {
  await page.goto('https://vielskerserier.dk/film/film-nyheder/den-sidste-viking-udtaget-til-prestigefyldt-filmfestival');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
});

//tests if jw player is loaded after marketing consent is given
test('test video player, total consent', async ({ page }) => {
  await page.goto('https://vielskerserier.dk/film/film-nyheder/den-sidste-viking-udtaget-til-prestigefyldt-filmfestival');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await page.evaluate(() => { 
    window.scrollBy(0, 1000);
  });
  await expect(page.locator('//div[@class="jw-media jw-reset"]')).toBeVisible();
});

//tests if jw player is shown on use of necessary consent
test('test video player, necessary consent', async ({ page }) => {
  await page.goto('https://vielskerserier.dk/film/film-nyheder/den-sidste-viking-udtaget-til-prestigefyldt-filmfestival');
  await page.getByRole('button', { name: 'Use necessary cookies only' }).click();
  await page.evaluate(() => { 
    window.scrollBy(0, 1000);
  });
  await expect(page.locator('//div[@class="jw-media jw-reset"]')).toBeVisible();
});

test('test ad placements on frontpage', async ({ page }) => {
  await page.goto('https://vielskerserier.dk');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await expect(page.locator('#responsive_1-1')).toBeVisible();
});

test('test ad placements on article', async ({ page }) => {
  await page.goto('https://vielskerserier.dk/film/film-anmeldelser/anmeldelse-cillian-murphy-kan-som-ingen-anden-fortaelle-en-hel-historie-med');
  await page.getByRole('button', { name: 'Allow all cookies' }).click();
  await expect(page.locator('#responsive_1-1')).toBeVisible();
});
