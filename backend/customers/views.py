from rest_framework import viewsets, filters, status  # type: ignore
from rest_framework.decorators import action  # type: ignore
from rest_framework.response import Response  # type: ignore
from django_filters.rest_framework import DjangoFilterBackend  # type: ignore
from django.db.models import Q  # type: ignore
from .models import Customer
from .serializers import CustomerSerializer, CustomerListSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing customers.
    
    Provides CRUD operations, search, and filtering for customers.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    ordering_fields = ['first_name', 'last_name', 'email', 'created_at']
    ordering = ['last_name', 'first_name']

    def get_serializer_class(self):
        """Return appropriate serializer based on action."""
        if self.action == 'list':
            return CustomerListSerializer
        return CustomerSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned customers,
        by filtering against query parameters.
        """
        queryset = Customer.objects.all()
        
        # Filter by active status
        is_active = self.request.query_params.get('is_active')
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active.lower() == 'true')
        
        # Custom search across multiple fields
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(
                Q(first_name__icontains=search) |
                Q(last_name__icontains=search) |
                Q(email__icontains=search) |
                Q(phone__icontains=search)
            )
        
        return queryset

    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Get customer statistics."""
        total_customers = Customer.objects.count()
        active_customers = Customer.objects.filter(is_active=True).count()
        inactive_customers = total_customers - active_customers
        
        return Response({
            'total_customers': total_customers,
            'active_customers': active_customers,
            'inactive_customers': inactive_customers,
        })

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        """Deactivate a customer."""
        customer = self.get_object()
        customer.is_active = False
        customer.save()
        
        return Response({
            'message': f'Customer {customer.full_name} has been deactivated.',
            'customer': CustomerSerializer(customer).data
        })

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        """Activate a customer."""
        customer = self.get_object()
        customer.is_active = True
        customer.save()
        
        return Response({
            'message': f'Customer {customer.full_name} has been activated.',
            'customer': CustomerSerializer(customer).data
        })