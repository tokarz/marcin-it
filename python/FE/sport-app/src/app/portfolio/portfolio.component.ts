import { Component, input } from '@angular/core';

@Component({
  selector: 'app-portfolio',
  imports: [],
  templateUrl: './portfolio.html',
  styleUrl: './portfolio.component.scss'
})
export class PortfolioComponent {

  userData = input<{name:string;age:string;nationality:string}>()
}
