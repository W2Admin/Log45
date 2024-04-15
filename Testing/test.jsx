// Import the necessary dependencies
import React from "react";
import { render, fireEvent } from "@testing-library/react";
import Button from "./Button";

describe("Button component", () => {
  it("renders a button with the correct text", () => {
    const { getByText } = render(<Button text="Click me" />);
    expect(getByText("Click me")).toBeInTheDocument();
  });

  it("invokes onClick handler when clicked", () => {
    const onClickMock = jest.fn();
    const { getByText } = render(
      <Button text="Click me" onClick={onClickMock} />
    );
    fireEvent.click(getByText("Click me"));
    expect(onClickMock).toHaveBeenCalledTimes(1);
  });
});
