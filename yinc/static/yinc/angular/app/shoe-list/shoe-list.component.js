
angular.
  module('shoeList').
  component('shoeList', {
    template:
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
                    '<div ng-controller="HttpGetController">' +
               			
               			'<button class="btn btn-success"  >Add to Cart</button>'+
               			
               			
               				
               			'<input type="hidden" name="productId" value="{{shoe.productId}}">'+
               			'<button class="btn btn-success" type="submit">Add to Wishlist</button>'+
               			'</form>'+
                    '</div>' +
               '</div>'+
            '</div>',
    controller: function ShoeListController($http) {
    	var self = this;
      $http.get('/yinc/api/product.json').then(function(response) {
        self.shoes = response.data;
      });
    }
  });