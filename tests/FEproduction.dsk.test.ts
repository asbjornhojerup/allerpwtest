import { test, expect } from '@playwright/test';
test.use({ viewport: { width: 1920, height: 1080 } });

test('test open menu, go to category', async ({ page }) => {
    await page.goto('https://femina.dk/');
    await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
    await page.getByRole('button', { name: 'Menu' }).click();
    await page.getByRole('link', { name: 'Stil', exact: true }).click();
});

test('test go to frontpage by clicking logo', async ({ page }) => {
    await page.goto('https://femina.dk/agenda');
    await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
    await page.getByLabel('Gå til forsiden').click();
});

test('test load more on category page', async ({ page }) => {
    await page.goto('https://femina.dk/agenda');
    await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
      await page.evaluate(() => { 
    window.scrollBy(0, 1000);
  });
    await page.getByRole('button', { name: 'Hent flere' }).click();
});

test('test open article on category page', async ({ page }) => {
    await page.goto('https://femina.dk/agenda');
    await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
    await page.locator('//*[@class="flex-grow relative mb-40 lg:mb-50 bg-sand-400 col-span-12 lg:col-span-4"]').first().click();
    await expect(page.locator('//*[@class="font-serif text-20 leading-26 py-20 max-w-710 md:text-24 md:leading-32 lg:text-24 lg:leading-34"]')).toBeVisible();
});

//test('test open article on frontpage', async ({ page }) => {
  //  await page.goto('https://femina.dk/');
    //await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
    //await page.locator('//*[@class="dre-item__text"]').first().click();
    //await expect(page.locator('//*[@class="font-serif text-20 leading-26 py-20 max-w-710 md:text-24 md:leading-32 lg:text-24 lg:leading-34"]')).toBeVisible();
//}); 

//tests if jw player is loaded after marketing consent is given
test('test video player, total consent', async ({ page }) => {
    await page.goto('https://femina.dk/agenda/karriere-og-penge/kendt-radiovaert-erstatter-sofie-linde-som-x-factor-vaert');
    await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
  await page.evaluate(() => { 
    window.scrollBy(0, 1000);
  });
  await expect(page.locator('//div[@class="jw-media jw-reset"]')).toBeVisible();
});

//tests if jw player is shown on use of necessary consent
test('test video player, necessary consent', async ({ page }) => {
  await page.goto('https://femina.dk/agenda/karriere-og-penge/kendt-radiovaert-erstatter-sofie-linde-som-x-factor-vaert');
  await page.getByRole('button', { name: 'Kun nødvendige cookies' }).click();
  await page.evaluate(() => { 
    window.scrollBy(0, 1000);
  });
  await expect(page.locator('//div[@class="jw-media jw-reset"]')).toBeVisible();
});

test('newsletter sign-up', async ({ page }) => {
  await page.goto('https://femina.dk/nyhedsbrev');
  await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
  await page.locator('//input[@id="email"]').fill('jjk@mailinator.com');
  await page.locator('//input[@id="firstname"]').fill('Jens');
  await page.locator('//input[@id="lastname"]').fill('Jensen');
  await page.locator('//input[@id="postal"]').fill('4070');
  await page.locator('//input[@id="terms"]').click();
  await page.locator('//button[@type="submit"]').click();
  await expect(page.getByText('Tak for tilmeldingen')).toBeVisible();
});

test('sign in to plus', async ({ page }) => {
  await page.goto('https://femina.dk/plus');
  await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
  await page.locator('//input[@id="email"]').fill('asbjornsjunk@gmail.com');
  await page.locator('//input[@id="password"]').fill('Gyg37cnr');
  await page.locator('//button[@type="submit"]').click();
  await expect(page.getByRole('link', { name: "Indstillinger", exact: true })).toBeVisible();
});

test('test ad placements on frontpage', async ({ page }) => {
  await page.goto('https://femina.dk');
  await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
  await expect(page.locator('#responsive_1-1')).toBeVisible();
});

test('test ad placements on article', async ({ page }) => {
  await page.goto('https://femina.dk/sundhed/jeg-er-paa-vej-hjem-til-dig-nu-sagde-vagtlaegen-i-telefonen-ingen-havde-regnet-med-noget');
  await page.getByRole('button', { name: 'Tillad alle cookies' }).click();
  await expect(page.locator('#responsive_1-1')).toBeVisible();
});
