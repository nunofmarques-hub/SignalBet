import { simpleTable } from '../components/tables.js';
export function renderPool(vm){ return `<div class="screen-section"><h3 class="section-title">Opportunity Pool</h3>${simpleTable(['Fixture','Market','Module','Score','Tier','Decision'], vm.rows)}</div>`; }
