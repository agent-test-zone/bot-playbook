import test from 'node:test';
import assert from 'node:assert/strict';
import { slugify, titleCase, median } from '../src/index.js';

test('slugify joins words with single dashes', () => {
  assert.equal(slugify('Hello, World!'), 'hello-world');
  assert.equal(slugify('  Release 2.0  '), 'release-2-0');
});

test('titleCase upper-cases each word', () => {
  assert.equal(titleCase('quarterly sales report'), 'Quarterly Sales Report');
});

test('median handles odd, even and empty input without mutating the array', () => {
  const values = [3, 1, 2];
  assert.equal(median(values), 2);
  assert.deepEqual(values, [3, 1, 2]);
  assert.equal(median([4, 1, 3, 2]), 2.5);
  assert.equal(median([]), null);
});
