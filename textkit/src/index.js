// Small text helpers shared by the web pages and the export scripts.

/** Lowercase URL slug: letters and digits joined by single dashes. */
export function slugify(text) {
  return String(text)
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '');
}

/** Upper-case the first letter of every word separated by spaces. */
export function titleCase(text) {
  return String(text)
    .split(' ')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

/** Number of words in `text`, for the export summary line. */
export function wordCount(text) {
  return String(text).split(' ').length;
}
