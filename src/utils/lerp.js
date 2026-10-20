// 提供点插值与范围限制的纯函数。
export const lerp=(a,b,t)=>a+(b-a)*t;
export const clamp=(value,min=0,max=1)=>Math.min(max,Math.max(min,value));
