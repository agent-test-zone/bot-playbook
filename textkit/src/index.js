// Small text helpers shared by the web pages and the export scripts.

/** Lowercase URL slug: letters and digits joined by single dashes. */
export function slugify(text) {
  return String(text)
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '');
}

/** Upper-case the first letter of every word separated by whitespace. */
export function titleCase(text) {
  return String(text).replace(/(^|\s)(\S)/g, (match, whitespace, character) =>
    whitespace + character.toUpperCase()
  );
}
