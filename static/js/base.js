function addTriangleTo(target) {
    var dimensions = target.getClientRects()[0];
    var pattern = Trianglify({
        width: dimensions.width,
        height: dimensions.height
    });
    target.style['background-image'] = 'url(' + pattern.png() + ')';
}

addTriangleTo(document.getElementById('canvas'));
