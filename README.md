# AppStore-crawler

### Todo List

##### 19-03-21

> apple app store 홈페이지(itunes preview)에서 모든 앱은 크롤링 할 수 있지만 검색기능 없음(x)
>
> itunes search api있음(https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/) -> 하지만 200개 제한
>
> 그래서 ios앱 검색해주는 https://fnd.io/#/ 이곳을 사용할까함.. 하지만 최신 앱들이 반영되어있는지 모르겠음,,
>
> -> 검색해보니 내가 하고자하는 검색어는 200개를 넘기지 않음,, 그래서 그냥 api사용. 그리고 위의 사이트도 뜯어보니 api를 이용해서 한계가 있었음.

> attribute 안주면  column은 아래와 같이 있음.
>
> ['advisories', 'appletvScreenshotUrls', 'artistId', 'artistName', 'artistViewUrl', 'artworkUrl100', 'artworkUrl512', 'artworkUrl60', 'averageUserRating', 'averageUserRatingForCurrentVersion', 'bundleId', 'contentAdvisoryRating', 'currency', 'currentVersionReleaseDate', 'description', 'features', 'fileSizeBytes', 'formattedPrice', 'genreIds', 'genres', 'ipadScreenshotUrls', 'isGameCenterEnabled', 'isVppDeviceBasedLicensingEnabled', 'kind', 'languageCodesISO2A', 'minimumOsVersion', 'price', 'primaryGenreId', 'primaryGenreName', 'releaseDate', 'releaseNotes', 'screenshotUrls', 'sellerName', 'sellerUrl', 'supportedDevices', 'trackCensoredName', 'trackContentRating', 'trackId', 'trackName', 'trackViewUrl', 'userRatingCount', 'userRatingCountForCurrentVersion', 'version', 'wrapperType']
>
> 여기서 우리가 필요한 것은 크게 두 가지
>
> 1. trackName: 앱 이름
> 2. description: 앱 설명

> 생각보다 너무 빨리 끝남..