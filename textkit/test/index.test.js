import test from 'node:test';
import assert from 'node:assert/strict';
import { slugify, titleCase } from '../src/index.js';

test('slugify joins words with single dashes', () => {
  assert.equal(slugify('Hello, World!'), 'hello-world');
  assert.equal(slugify('  Release 2.0  '), 'release-2-0');
});

test('titleCase upper-cases each word', () => {
  assert.equal(titleCase('quarterly sales report'), 'Quarterly Sales Report');
});

test('slugify returns an empty slug for punctuation only and keeps digits', () => {
  assert.equal(slugify('!!! ...'), '');
  assert.equal(slugify('2026'), '2026');
  assert.equal(slugify('v2 -- 3'), 'v2-3');
});