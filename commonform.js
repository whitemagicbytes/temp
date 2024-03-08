import React from 'react';
import { useForm } from 'react-hook-form'; // Assuming you're using it

function CommonForm({ activeTab, onSubmit }) {
  const { register, handleSubmit, formState: { errors } } = useForm();

  const fieldDefinitions = {
    a: {
      regex: /^[a-zA-Z]+$/,
      placeholder: 'Enter text only (a-z, A-Z)',
    },
    b: {
      regex: /^\d{3}-\d{2}-\d{4}$/,
      placeholder: 'Enter in format XXX-XX-XXXX (b)',
    },
    c: {
      regex: /^.+@.+\..+$/,
      placeholder: 'Enter a valid email address (c)',
    },
    // Add similar definitions for fields d and e
    d: {
      regex: /^[0-9]+$/,
      placeholder: 'Enter only numbers (d)',
    },
    e: {
      regex: /^(http|https):\/\/[^\s]+/,
      placeholder: 'Enter a valid URL (e)',
    },
  };

  const fieldsByTab = {
    tab1: ['a', 'b', 'c', 'd', 'e'],
    tab2: ['a', 'b', 'c', 'd', 'f', 'g'],
    tab3: ['a', 'b', 'c', 'd', 'f', 'i'],
  };

  const activeFields = fieldsByTab[activeTab] || [];

  // Extract form data based on active fields
  const getFormData = (data) => {
    const formData = {};
    activeFields.forEach((field) => {
      formData[field] = data[field];
    });
    return formData;
  };

  return (
    <form onSubmit={handleSubmit(() => onSubmit(getFormData(register())))}>
      {activeFields.map((field) => (
        <div key={field}>
          <label htmlFor={field}>{field}</label>
          <input
            type="text"
            id={field}
            {...register(field, {
              required: true,
              pattern: fieldDefinitions[field]?.regex, // Apply regex validation if defined
            })}
            placeholder={fieldDefinitions[field]?.placeholder} // Set placeholder if defined
          />
          {errors[field] && <span className="error">{errors[field].message}</span>}
        </div>
      ))}
      <button type="submit">Submit {activeTab}</button>
    </form>
  );
}

export default CommonForm;
