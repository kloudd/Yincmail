'<div class="col-lg-12" ng-repeat="shoe in $ctrl.shoes">' + 
         '<div class="col-lg-4">' +
            '<img ng-src="/static/{{shoe.imageUrl}}" height="50px" width="50px">'+
                        '<br>'+
                        'Name:{{shoe.name}}'+
                        '<br>'+
                        'Price{{shoe.price}}'+
                        '<br>'+
                        'Weight{{shoe.weight}}'+
                        '<br>'+
                        'Category{{shoe.category}}'+
                        '<br>'+
                        
                        '<button class="btn btn-success"  >Add to Cart</button>'+
                        
                        '<form name="myform" id="myform" method="POST" action="/yinc/controller/addToWishList/">'+
                           
                        '<input type="hidden" name="productId" value="{{shoe.productId}}">'+
                        '<button class="btn btn-success" type="submit">Add to Wishlist</button>'+
                        '</form>'+
               '</div>'+
            '</div>',