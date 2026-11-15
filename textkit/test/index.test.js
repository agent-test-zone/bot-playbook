import test from 'node:test';
import assert from 'node:assert/strict';
import { slugify, titleCase } from '../src/index.js';

test('slugify joins words with single dashes', () => {
  assert.equal(slugify('Hello, World!'), 'hello-world');
  assert.equal(slugify('  Release 2.0  '), 'release-2-0');
});

test('titleCase upper-cases each word', () => {
  assert.equal(titleCase('quarterly sales report'), 'Quarterly Sales Report');
  assert.equal(titleCase('hello\tworld'), 'Hello\tWorld');
  assert.equal(titleCase('hello\nworld'), 'Hello\nWorld');
  assert.equal(titleCase('  hello  world  '), '  Hello  World  ');
});
