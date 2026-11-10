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

/** Median of finite numbers, or null for empty input. Leaves the input unchanged. */
export function median(values) {
  if (values.length === 0) return null;
  const sorted = [...values].sort((a, b) => a - b);
  const middle = Math.floor(sorted.length / 2);
  return sorted.length % 2 === 1
    ? sorted[middle]
    : (sorted[middle - 1] + sorted[middle]) / 2;
}
