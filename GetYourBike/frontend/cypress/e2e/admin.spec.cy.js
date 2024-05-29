describe('Create Rent Bicycle', () => {
    beforeEach(() => {
      cy.visit('http://localhost:3000/admin');
    })
  
    it('creates a new rent bicycle and displays it in the list', () => {
      cy.contains('Add New Bicycle').click();
  

      cy.get('input[data-testid="brand-input"]').type('Giant');
      cy.get('input[data-testid="model-input"]').type('XTC 800');
      cy.get('div[role="combobox"]').click({force:true})
      cy.contains('Off-road').click()
      cy.get('input[data-testid="reserved-dates-input"]').type('2024-06-01');
      cy.get('input[data-testid="price-per-day-input"]').type('25.0');

      cy.intercept('POST', '/api/rentBicycles/', (req) => {
        req.reply((res) => {
          res.send({
            id: 9,
            brand: req.body.brand,
            model: req.body.model,
            category: req.body.category,
            reservedDates: req.body.reservedDates,
            pricePerDay: req.body.pricePerDay
          });
        });
      }).as('createRentBicycle');
  
      cy.contains('button', 'Save').click();
  
      cy.wait('@createRentBicycle').then((interception) => {

        expect(interception.response.statusCode).to.eq(201);
  
        expect(interception.response.body).to.have.property('id');
        expect(interception.response.body.brand).to.eq('Giant');
        expect(interception.response.body.model).to.eq('XTC 800');
      });

      cy.visit('http://localhost:3000/rent');
      cy.contains('Giant').should('be.visible');
      cy.contains('XTC 800').should('be.visible');
      cy.contains('25').should('be.visible');
    })
  })
  