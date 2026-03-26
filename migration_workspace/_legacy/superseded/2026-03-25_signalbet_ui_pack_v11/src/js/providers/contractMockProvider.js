import { pages } from '../../data/mock-data.js';
export const contractMockProvider = { getPageData: (page) => pages[page] || {} };
