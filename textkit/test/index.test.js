import test from 'node:test';
import assert from 'node:assert/strict';
import { slugify, titleCase, wordCount } from '../src/index.js';

test('slugify joins words with single dashes', () => {
  assert.equal(slugify('Hello, World!'), 'hello-world');
  assert.equal(slugify('  Release 2.0  '), 'release-2-0');
});

test('titleCase upper-cases each word', () => {
  assert.equal(titleCase('quarterly sales report'), 'Quarterly Sales Report');
});

test('wordCount counts the words of a sentence', () => {
  assert.equal(wordCount('ship the order today'), 4);
});

test('wordCount ignores extra whitespace and counts empty text as zero', () => {
  assert.equal(wordCount(''), 0);
  assert.equal(wordCount('  ship\tthe\norder  '), 3);
});
