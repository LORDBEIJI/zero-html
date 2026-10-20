// 以唯一帧循环调度全站动画并在后台暂停。
const callbacks=new Set();let handle=0;
function frame(time){for(const callback of callbacks)callback(time);handle=callbacks.size&&!document.hidden?requestAnimationFrame(frame):0;}
export function addFrame(callback){callbacks.add(callback);if(!handle&&!document.hidden)handle=requestAnimationFrame(frame);return()=>{callbacks.delete(callback);if(!callbacks.size){cancelAnimationFrame(handle);handle=0;}};}
document.addEventListener('visibilitychange',()=>{if(document.hidden){cancelAnimationFrame(handle);handle=0;}else if(callbacks.size&&!handle)handle=requestAnimationFrame(frame);});
