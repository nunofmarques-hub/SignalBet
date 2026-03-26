import { bootstrap } from './services/uiDataService.js';
import { homeViewModel } from './viewmodels/homeViewModel.js';
import { renderHome } from './pages/home.js';

const root = document.getElementById('app');
bootstrap('real_read_protected').then(data=>{
  root.innerHTML = renderHome(homeViewModel(data));
});
