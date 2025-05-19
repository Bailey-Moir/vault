import { Plugin } from "obsidian";

export default class LatexCalloutsPlugin extends Plugin {
	async onload() {
		const processIcons = (element: HTMLElement) => {
			let handle = setInterval(async () => {
				let svgs = element.findAll(`svg.svg-icon`);
				svgs = svgs.filter(svg => svg.parentElement?.classList.contains('callout-icon'))
		
				//if (svgs.length > 0) clearInterval(handle);
		
				svgs.forEach((svg) => {
					let rawTitle = svg.parentElement?.parentElement?.parentElement?.getAttr("data-callout")!;
					let titleText = rawTitle.charAt(0).toUpperCase() + rawTitle.replace(/-/g,' ').slice(1);

					let words = rawTitle.split('-');
					let title = words.map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
		
					let titleElement = svg.parentElement?.nextElementSibling!;
					
					if (titleElement.textContent == titleText) titleElement.textContent = "";
					
					let b = document.createElement("b");
					b.textContent = title + " "
					b.classList.add("callout-latex-title");
					
					titleElement.prepend(b);
		
					svg.remove();
					svgs.remove(svg)
				});
			}, 10);
		
			setTimeout(() => {clearInterval(handle)}, 10000);
		};
		this.registerMarkdownPostProcessor(processIcons);

		this.app.workspace.on("layout-change", () => {
			this.app.workspace.iterateAllLeaves((leaf) => {
				if (leaf.view.getViewType() === "markdown") {
					const container = leaf.view.containerEl;
					processIcons(container);
				}
			});
		});
	}
}
