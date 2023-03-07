import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Form, Button, FormGroup, FormLabel, Col, FormCheck } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import FormContainer from "../components/FormContainer";
import CheckoutSteps from "../components/CheckoutSteps";
import { savePaymentMethod } from "../actions/cartActions";

function PaymentScreen() {
  const cart = useSelector(state => state.cart)
  const { shippingAddress } = cart

  const dispatch = useDispatch()
  const navigate = useNavigate()

  const [paymentMethod, setPaymentMethod] = useState("PayPal")

  if (!shippingAddress.address) {
    navigate("/shipping")
  }

  const submitHandler = (e) => {
    e.preventDefault()
    dispatch(savePaymentMethod(paymentMethod))
    navigate("/placeorder")

  }

  return (
    <FormContainer>
      <CheckoutSteps step1 step2 step3 />

      <Form onSubmit={submitHandler}>
        <FormGroup>
          <FormLabel as='legend'>Select method</FormLabel>
          <Col>
            <FormCheck
              className="mt-3"
              type='radio'
              label='PayPal or Credit Card'
              id='paypal'
              name='paymentMathod'
              checked onChange={(e) => setPaymentMethod(e.target.value)}
            >

            </FormCheck>
          </Col>
        </FormGroup>

        <Button type='submit' variant='primary' className="mt-3">
          Continue
        </Button>

      </Form>

    </FormContainer>
  )
}

export default PaymentScreen
