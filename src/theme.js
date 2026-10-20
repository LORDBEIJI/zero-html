// 在页面绘制前恢复本地主题以避免闪烁。
try{document.documentElement.dataset.theme=localStorage.getItem('wenmai-theme')||'ink';}catch{document.documentElement.dataset.theme='ink';}
if(navigator.connection?.saveData||/2g|3g/.test(navigator.connection?.effectiveType||''))document.documentElement.dataset.network='slow';
