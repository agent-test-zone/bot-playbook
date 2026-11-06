import test from 'node:test';
import assert from 'node:assert/strict';
import { slugify, titleCase } from '../src/index.js';

test('slugify joins words with single dashes', () => {
  assert.equal(slugify('Hello, World!'), 'hello-world');
  assert.equal(slugify('  Release 2.0  '), 'release-2-0');
});

test('slugify folds accented Latin letters to plain letters', () => {
  assert.equal(slugify('Café Crème'), 'cafe-creme');
  assert.equal(slugify('naïve'), 'naive');
  assert.equal(slugify('Über'), 'uber');
});

test('slugify folds decomposed accents the same way as precomposed ones', () => {
  assert.equal(slugify('Cafe\u0301 Cre\u0300me'), 'cafe-creme');
  assert.equal(slugify('Cafe\u0301 Cre\u0300me'), slugify('Café Crème'));
});

test('titleCase upper-cases each word', () => {
  assert.equal(titleCase('quarterly sales report'), 'Quarterly Sales Report');
});
