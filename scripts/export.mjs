// 将独立运行所需的静态文件导出到工作区 dist 目录。
import fs from'node:fs/promises';import path from'node:path';
const runtime=['index.html','gallery.html','stories.html','about.html','craft','styles','src','vendor','assets'];await fs.mkdir('dist',{recursive:true});for(const name of runtime)await fs.cp(name,path.join('dist',name),{recursive:true,filter:source=>!source.endsWith('-source.png')});process.stdout.write('静态部署文件已同步到 dist/。\n');
