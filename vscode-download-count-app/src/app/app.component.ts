import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';


@Component({
  selector: 'app-root',
  template: `

    {{extensions | json }}

    <ul>
    <li *ngFor="let extension of extensionsArray">
     {{extension.name}}
    </li>
   </ul>

  `,
  styles: []
})
export class AppComponent {
  extensions = []
  extensionsArray = []
  title = 'app';

  constructor(private http: HttpClient) {
    this.http.get("./assets/extensions.json").subscribe(res => {

      this.extensions = Object.keys(res)

      this.extensions.forEach(extensionName => {
        this.extensionsArray.push(res[extensionName])
      });

    })
    
  }

  keys() : Array<string> {
    return Object.keys(this.extensions);
  }


}
