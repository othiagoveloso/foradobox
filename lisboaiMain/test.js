<meta property="og:url"           content="https://www.your-domain.com/your-page.html" />
<meta property="og:type"          content="website" />
<meta property="og:title"         content="Your Website Title" />
<meta property="og:description"   content="Your description" />
<meta property="og:image"         content="https://www.your-domain.com/path/image.jpg" />



var property = ['url', 'type', 'title', 'description', 'image']; 

var content = ['http://haforadobox.herokuapp.com', 'website', 'como morar em portugal','saiba mais', 'image'];



for(var i = 0; i <= property.length; i++ ){

    var result = property[i] + ':' + content[i]

    property = content

}
