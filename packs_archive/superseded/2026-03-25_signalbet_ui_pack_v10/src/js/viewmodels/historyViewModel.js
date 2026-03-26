export function createHistoryViewModel(data){ return { items:data.history, wins:data.history.filter(x=>x.result==='WIN').length, losses:data.history.filter(x=>x.result==='LOSS').length }; }
